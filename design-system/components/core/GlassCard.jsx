export function GlassCard({children,strong=false,glow=false,style}){
const cls=strong?'glass-strong':'glass';
return <div className={cls} style={{padding:'24px',boxShadow:glow?'inset 0 1px 1px var(--glass-highlight), var(--glass-shadow), var(--glass-glow)':undefined,...style}}>{children}</div>;
}
