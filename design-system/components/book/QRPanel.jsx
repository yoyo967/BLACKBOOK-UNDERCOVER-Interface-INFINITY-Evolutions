export function QRPanel({url,size=96}){
return <div style={{display:'flex',alignItems:'center',gap:'16px'}}>
<div style={{width:size,height:size,background:'var(--fg)',borderRadius:'8px',display:'grid',placeItems:'center',flexShrink:0}}>
<span style={{fontFamily:'var(--font-mono)',fontSize:'10px',color:'var(--bg)',textAlign:'center',padding:'4px'}}>QR</span>
</div>
<span style={{fontFamily:'var(--font-mono)',fontSize:'12px',color:'var(--fg-mute)',wordBreak:'break-all'}}>{url}</span>
</div>;
}
