export function ChapterKicker({series,band}){
return <div style={{display:'flex',flexDirection:'column',gap:'4px',alignItems:'center',textAlign:'center'}}>
<span style={{fontFamily:'var(--font-mono)',fontSize:'13px',letterSpacing:'0.2em',textTransform:'uppercase',color:'var(--fg-mute)'}}>{series}</span>
{band&&<span style={{fontFamily:'var(--font-mono)',fontSize:'12px',letterSpacing:'0.16em',textTransform:'uppercase',color:'var(--signal-bright)'}}>{band}</span>}
</div>;
}
