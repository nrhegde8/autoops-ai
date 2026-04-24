export default function OrderCard({ o, theme }) {

  const statusColor =
    o.status === "Delivered" ? "#22c55e" :
    o.status === "In Transit" ? "#facc15" :
    "#ef4444";

  return (
    <div style={{
      padding:20,
      borderRadius:20,
      background:"#fff",
      boxShadow: theme.shadow,
      width:260,
      transition:"0.2s",
      cursor:"pointer"
    }}
    onMouseEnter={e=>e.currentTarget.style.transform="scale(1.03)"}
    onMouseLeave={e=>e.currentTarget.style.transform="scale(1)"}
    >

      <div style={{display:"flex",justifyContent:"space-between"}}>
        <h3>{o.product_name}</h3>
        <span style={{
          background:statusColor,
          color:"#fff",
          padding:"4px 10px",
          borderRadius:20,
          fontSize:12
        }}>
          {o.status}
        </span>
      </div>

      <p>📍 {o.city}</p>
      <p>🚚 {o.courier}</p>

      <div style={{
        height:6,
        background:"#eee",
        borderRadius:10,
        marginTop:10
      }}>
        <div style={{
          width: o.status==="Delivered"?"100%":o.status==="In Transit"?"60%":"20%",
          height:"100%",
          borderRadius:10,
          background: theme.primary
        }}/>
      </div>
    </div>
  );
}