export default function Sidebar({ tab, setTab, theme }) {

  const tabs = ["dashboard","orders","analytics","shipments","ai","settings"];

  return (
    <div style={{
      width:240,
      padding:20,
      background:"#fff",
      borderRight:"1px solid #eee"
    }}>
      <h2 style={{color:theme.primary}}>AutoOps</h2>

      {tabs.map(t=>(
        <div
          key={t}
          onClick={()=>setTab(t)}
          style={{
            padding:12,
            margin:"10px 0",
            borderRadius:12,
            cursor:"pointer",
            background: tab===t ? theme.gradient : "transparent",
            color: tab===t ? "#fff" : "#444",
            transition:"0.2s"
          }}
        >
          {t.toUpperCase()}
        </div>
      ))}
    </div>
  );
}