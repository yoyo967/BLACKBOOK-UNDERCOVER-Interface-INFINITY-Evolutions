export function Badge({children,tone='neutral',mono=false}){
const tones={
neutral:{background:'var(--bg-surface)',color:'var(--fg-mute)',border:'1px solid var(--line)'},
signal:{background:'rgba(6,182,212,.12)',color:'var(--signal-bright)',border:'1px solid rgba(6,182,212,.35)'},
outline:{background:'transparent',color:'var(--fg-dim)',border:'1px solid var(--line)'},
};
return <span style={{display:'inline-flex',alignItems:'center',gap:'6px',padding:'4px 12px',borderRadius:'var(--radius-full)',fontSize:'12px',fontFamily:mono?'var(--font-mono)':'var(--font-body)',letterSpacing:mono?'0.06em':'0.02em',textTransform:mono?'uppercase':'none',...tones[tone]}}>{children}</span>;
}
