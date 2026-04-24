import React, { useState, useEffect, useRef } from "react";

export default function App() {

  const themes = {
    orange: { primary: "#ff6b00", secondary: "#fff7f0" },
    gold: { primary: "#d4af37", secondary: "#fffdf5" },
    green: { primary: "#00c853", secondary: "#f4fff7" }
  };

  const [themeName, setThemeName] = useState("orange");
  const [dark, setDark] = useState(false);
  const theme = themes[themeName];

  const cardBg = dark ? "#1e293b" : "white";
  const textColor = dark ? "white" : "#111";

  const [tab, setTab] = useState("dashboard");
  const [orders, setOrders] = useState([]);
  const [filtered, setFiltered] = useState([]);

  const [search, setSearch] = useState("");
  const [cityFilter, setCityFilter] = useState("all");

  const [product, setProduct] = useState("");
  const [weight, setWeight] = useState("");
  const [city, setCity] = useState("");

  const [chatInput, setChatInput] = useState("");
  const [messages, setMessages] = useState([
    { sender: "bot", text: "🚀 AutoOps AI Ready" }
  ]);
  const [loading, setLoading] = useState(false);

  const chatRef = useRef();

  const fetchOrders = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/orders/");
    const data = await res.json();

    const enriched = data.map(o => ({
      ...o,
      status: ["Pending","In Transit","Delivered"][Math.floor(Math.random()*3)],
      progress: Math.floor(Math.random()*100)
    }));

    setOrders(enriched);
    setFiltered(enriched);
  };

  useEffect(()=>{ fetchOrders(); },[]);

  useEffect(()=>{
    let f = [...orders];

    f = f.filter(o =>
      o.product_name?.toLowerCase().includes(search.toLowerCase()) ||
      o.city?.toLowerCase().includes(search.toLowerCase())
    );

    if (cityFilter !== "all") {
      f = f.filter(o => o.city === cityFilter);
    }

    setFiltered(f);

  },[search,orders,cityFilter]);

  const createOrder = async () => {
    if (!product || !weight || !city) return;

    await fetch("http://127.0.0.1:8000/api/orders/create/", {
      method:"POST",
      headers:{ "Content-Type":"application/json" },
      body: JSON.stringify({ product_name:product, weight, city })
    });

    fetchOrders();
    setProduct(""); setWeight(""); setCity("");
  };

  const sendChat = async () => {
    if (!chatInput) return;

    setMessages(m=>[...m,{ sender:"user", text:chatInput }]);
    setChatInput("");
    setLoading(true);

    const res = await fetch("http://127.0.0.1:8001/chat",{
      method:"POST",
      headers:{ "Content-Type":"application/json" },
      body: JSON.stringify({ message: chatInput })
    });

    const data = await res.json();

    let reply = "";

    if (data.tool_used === "create_order") {
      reply = "✅ Order created successfully";
      setTimeout(fetchOrders,500);
    }
    else if (data.tool_used === "send_email") {
      reply = "📩 Email sent successfully";
    }
    else {
      reply = data.response || "⚠️ Something went wrong";
    }

    setMessages(m=>[...m,{ sender:"bot", text:reply }]);
    setLoading(false);
  };

  useEffect(()=>{
    chatRef.current?.scrollIntoView({ behavior:"smooth" });
  },[messages]);

  const statusColor = s =>
    s==="Delivered" ? "#22c55e" :
    s==="In Transit" ? "#facc15" :
    "#ef4444";

  const Sidebar = () => (
    <div style={{...styles.sidebar, background: dark ? "#020617" : "white"}}>
      <h2 style={{color:theme.primary}}>AutoOps</h2>

      {["dashboard","orders","analytics","shipments","ai","settings"].map(t=>(
        <div
          key={t}
          onClick={()=>setTab(t)}
          style={{
            ...styles.nav,
            background: tab===t ? theme.primary : "transparent",
            color: tab===t ? "white" : dark ? "#ccc" : "#555"
          }}
        >
          {t.toUpperCase()}
        </div>
      ))}
    </div>
  );

  const Card = ({children}) => (
    <div style={{...styles.card, background:cardBg, color:textColor}}>
      {children}
    </div>
  );

  return (
    <div style={{
      ...styles.app,
      background: dark ? "#0f172a" : theme.secondary,
      color: textColor
    }}>

      <Sidebar />

      <div style={styles.main}>

        {/* DASHBOARD */}
        {tab==="dashboard" && (
          <>
            <h1>Dashboard</h1>

            <div style={styles.grid}>
              <Card><h2>{orders.length}</h2><p>Orders</p></Card>
              <Card><h2>{[...new Set(orders.map(o=>o.city))].length}</h2><p>Cities</p></Card>
            </div>

            <div style={styles.form}>
              <input placeholder="Product" value={product} onChange={e=>setProduct(e.target.value)} style={styles.input}/>
              <input placeholder="Weight" value={weight} onChange={e=>setWeight(e.target.value)} style={styles.input}/>
              <input placeholder="City" value={city} onChange={e=>setCity(e.target.value)} style={styles.input}/>
              <button style={styles.btn} onClick={createOrder}>Create</button>
            </div>
          </>
        )}

        {/* ORDERS */}
        {tab==="orders" && (
          <>
            <h1>Orders</h1>

            <input placeholder="Search..." value={search} onChange={e=>setSearch(e.target.value)} style={styles.input}/>

            <select value={cityFilter} onChange={e=>setCityFilter(e.target.value)} style={styles.input}>
              <option value="all">All Cities</option>
              {[...new Set(orders.map(o=>o.city))].map((c,i)=>(
                <option key={i}>{c}</option>
              ))}
            </select>

            <div style={styles.grid}>
              {filtered.map((o,i)=>(
                <Card key={i}>
                  <h3>{o.product_name}</h3>
                  <p>📍 {o.city}</p>
                  <p>🚚 {o.courier}</p>
                  <span style={{...styles.badge, background:statusColor(o.status)}}>{o.status}</span>
                </Card>
              ))}
            </div>
          </>
        )}

        {/* ANALYTICS */}
        {tab==="analytics" && (
          <>
            <h1>Analytics</h1>

            {orders.length === 0 ? (
              <Card>
                <h2>🚧 Coming Soon</h2>
                <p>Analytics module is under development</p>
              </Card>
            ) : (
              <Card>
                <h3>Orders per City</h3>

                {[...new Set(orders.map(o=>o.city))].map((c,i)=>{
                  const count = orders.filter(o=>o.city===c).length;

                  return (
                    <div key={i} style={{marginBottom:10}}>
                      <p>{c}</p>
                      <div style={{background:"#ddd", height:8, borderRadius:10}}>
                        <div style={{
                          width:`${count*20}px`,
                          height:"100%",
                          background:theme.primary,
                          borderRadius:10
                        }}/>
                      </div>
                    </div>
                  );
                })}
              </Card>
            )}
          </>
        )}

        {/* SHIPMENTS */}
        {tab==="shipments" && (
          <>
            <h1>Shipments</h1>

            {orders.slice(0,5).map((o,i)=>(
              <Card key={i}>
                <h3>{o.product_name}</h3>
                <p>{o.city}</p>
                <p>Status: {o.status}</p>
                <div style={styles.progress}>
                  <div style={{...styles.progressBar, width:`${o.progress}%`, background:theme.primary}}/>
                </div>
              </Card>
            ))}
          </>
        )}

        {/* AI */}
        {tab==="ai" && (
          <>
            <h1>AI Assistant</h1>

            <div style={styles.promptRow}>
              {[
                "create order for shoes weight 2 city chennai",
                "send email to abc@gmail.com subject hello body hi"
              ].map((p,i)=>(
                <div key={i} style={styles.prompt} onClick={()=>setChatInput(p)}>
                  {p}
                </div>
              ))}
            </div>

            <Card>
              <p>💡 Use chatbot on right →</p>
            </Card>
          </>
        )}

        {/* SETTINGS */}
        {tab==="settings" && (
          <>
            <h1>Settings</h1>

            <h3>Theme</h3>
            {Object.keys(themes).map(t=>(
              <button key={t} onClick={()=>setThemeName(t)} style={{...styles.btn, marginRight:10}}>
                {t}
              </button>
            ))}

            <h3 style={{marginTop:20}}>Dark Mode</h3>
            <button style={styles.btn} onClick={()=>setDark(!dark)}>
              {dark ? "ON" : "OFF"}
            </button>
          </>
        )}

      </div>

      {/* CHAT */}
      <div style={styles.chat}>
        <div style={styles.chatBox}>
          {messages.map((m,i)=>(
            <div key={i} style={{textAlign:m.sender==="user"?"right":"left"}}>
              <div style={{
                ...styles.bubble,
                background:m.sender==="user"?theme.primary:"#ddd",
                color:m.sender==="user"?"white":"black"
              }}>
                {m.text}
              </div>
            </div>
          ))}
          {loading && <p>🤖 Thinking...</p>}
          <div ref={chatRef}/>
        </div>

        <input value={chatInput} onChange={e=>setChatInput(e.target.value)} style={styles.input}/>
        <button style={styles.btn} onClick={sendChat}>Send</button>
      </div>

    </div>
  );
}

const styles = {
  app:{ display:"flex", height:"100vh", fontFamily:"Inter" },
  sidebar:{ width:220, padding:20 },
  nav:{ padding:12, margin:"8px 0", borderRadius:12, cursor:"pointer" },
  main:{ flex:1, padding:20, overflowY:"auto" },
  grid:{ display:"flex", gap:20, flexWrap:"wrap" },
  card:{ padding:20, borderRadius:16 },
  form:{ display:"flex", gap:10, marginTop:20 },
  input:{ padding:10, borderRadius:10, border:"none", marginTop:10 },
  btn:{ padding:10, borderRadius:10, border:"none", background:"#ff6b00", color:"white", cursor:"pointer" },
  badge:{ padding:"4px 10px", borderRadius:20, color:"white", fontSize:12 },
  progress:{ height:6, background:"#eee", borderRadius:10, marginTop:10 },
  progressBar:{ height:"100%", borderRadius:10 },
  chat:{ width:320, padding:10, display:"flex", flexDirection:"column" },
  chatBox:{ flex:1, overflowY:"auto" },
  bubble:{ padding:10, borderRadius:12, margin:5 },
  promptRow:{ display:"flex", gap:10, marginBottom:10 },
  prompt:{ padding:6, background:"#eee", borderRadius:20, cursor:"pointer" }
};