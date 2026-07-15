export function DualLayerBlock({labelA='Schicht A',titleA,textA,labelB='Schicht B',titleB,textB}){
const wrap={display:'grid',gridTemplateColumns:'1fr 1fr',gap:'1px',background:'var(--line)',border:'1px solid var(--line)',borderRadius:'var(--radius)',overflow:'hidden'};
const pane=(bg,fg)=>({background:bg,padding:'24px',display:'flex',flexDirection:'column',gap:'8px'});
return <div style={wrap}>
<div style={pane('var(--fg)')}>
<span style={{fontFamily:'var(--font-mono)',fontSize:'11px',letterSpacing:'0.16em',textTransform:'uppercase',color:'var(--signal-deep)'}}>{labelA}</span>
<strong style={{fontFamily:'var(--font-display)',fontSize:'18px',color:'#020617'}}>{titleA}</strong>
<p style={{fontFamily:'var(--font-body)',fontSize:'14px',color:'#334155',lineHeight:1.6,margin:0}}>{textA}</p>
</div>
<div style={pane('var(--bg-elevated)')}>
<span style={{fontFamily:'var(--font-mono)',fontSize:'11px',letterSpacing:'0.16em',textTransform:'uppercase',color:'var(--signal-bright)'}}>{labelB}</span>
<strong style={{fontFamily:'var(--font-display)',fontSize:'18px',color:'var(--fg)'}}>{titleB}</strong>
<p style={{fontFamily:'var(--font-body)',fontSize:'14px',color:'var(--fg-mute)',lineHeight:1.6,margin:0}}>{textB}</p>
</div>
</div>;
}
