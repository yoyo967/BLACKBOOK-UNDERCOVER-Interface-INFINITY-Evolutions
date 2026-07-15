export function Divider({label,style}){
if(!label) return <hr style={{border:'none',borderTop:'1px solid var(--line)',margin:'24px 0',...style}}/>;
return <div style={{display:'flex',alignItems:'center',gap:'12px',margin:'24px 0',...style}}>
<div style={{flex:1,height:'1px',background:'linear-gradient(90deg,transparent,var(--line))'}}/>
<span style={{fontFamily:'var(--font-mono)',fontSize:'11px',letterSpacing:'0.16em',textTransform:'uppercase',color:'var(--signal-bright)'}}>{label}</span>
<div style={{flex:1,height:'1px',background:'linear-gradient(270deg,transparent,var(--line))'}}/>
</div>;
}
