export default function ChatPanel({
  messages, chatInput, setChatInput, sendChat, theme, loading
}) {

  return (
    <div style={{
      width:360,
      display:"flex",
      flexDirection:"column",
      borderLeft:"1px solid #eee",
      padding:10,
      background:"#fff"
    }}>

      <div style={{
        fontWeight:"bold",
        marginBottom:10,
        color:theme.primary
      }}>
        🤖 AI Assistant
      </div>

      <div style={{flex:1, overflowY:"auto"}}>
        {messages.map((m,i)=>(
          <div key={i} style={{textAlign:m.sender==="user"?"right":"left"}}>
            <div style={{
              display:"inline-block",
              padding:10,
              margin:5,
              borderRadius:12,
              background: m.sender==="user" ? theme.primary : "#eee",
              color: m.sender==="user" ? "#fff" : "#000"
            }}>
              {m.text}
            </div>
          </div>
        ))}
        {loading && <p>Typing...</p>}
      </div>

      <input
        value={chatInput}
        onChange={e=>setChatInput(e.target.value)}
        placeholder="Type command..."
        style={{
          padding:10,
          borderRadius:10,
          border:"1px solid #ddd",
          marginTop:10
        }}
      />

      <button
        onClick={sendChat}
        style={{
          marginTop:10,
          padding:10,
          borderRadius:10,
          border:"none",
          background: theme.gradient,
          color:"#fff"
        }}
      >
        Send
      </button>

    </div>
  );
}