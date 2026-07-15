export function Button({variant='primary',size='md',children,disabled,onClick,style}){
const sizes={sm:{padding:'8px 16px',fontSize:'13px'},md:{padding:'12px 24px',fontSize:'15px'},lg:{padding:'16px 32px',fontSize:'16px'}};
const base={fontFamily:'var(--font-body)',fontWeight:600,letterSpacing:'0.01em',borderRadius:'var(--radius-full)',border:'1px solid transparent',cursor:disabled?'not-allowed':'pointer',opacity:disabled?0.45:1,transition:'all var(--duration-standard) var(--ease-standard)',display:'inline-flex',alignItems:'center',gap:'8px',...sizes[size]};
const variants={
primary:{background:'var(--signal)',color:'#01131a',boxShadow:'0 0 24px rgba(6,182,212,.35)'},
secondary:{background:'transparent',color:'var(--fg)',border:'1px solid var(--line)'},
ghost:{background:'transparent',color:'var(--signal-bright)',border:'1px solid transparent'},
};
return <button disabled={disabled} onClick={onClick} style={{...base,...variants[variant],...style}}
onMouseEnter={e=>{if(disabled)return;if(variant==='primary')e.currentTarget.style.background='var(--signal-bright)';if(variant==='secondary')e.currentTarget.style.borderColor='var(--signal)';if(variant==='ghost')e.currentTarget.style.color='var(--fg)';}}
onMouseLeave={e=>{if(disabled)return;if(variant==='primary')e.currentTarget.style.background='var(--signal)';if(variant==='secondary')e.currentTarget.style.borderColor='var(--line)';if(variant==='ghost')e.currentTarget.style.color='var(--signal-bright)';}}
>{children}</button>;
}
