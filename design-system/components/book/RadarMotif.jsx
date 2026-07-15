export function RadarMotif({size=200,pulse=true}){
const rings=[1,0.75,0.5,0.28];
return <div style={{position:'relative',width:size,height:size}}>
{rings.map((r,i)=><div key={i} style={{position:'absolute',inset:0,margin:'auto',width:size*r,height:size*r,borderRadius:'50%',border:'1px solid rgba(6,182,212,'+(0.15+i*0.12)+')'}}/>)}
<div style={{position:'absolute',inset:0,margin:'auto',width:'6px',height:'6px',borderRadius:'50%',background:'var(--signal-bright)',boxShadow:'0 0 24px 6px rgba(34,211,238,.6)',animation:pulse?'radarPulse 2.4s ease-in-out infinite':'none'}}/>
<style>{'@keyframes radarPulse{0%,100%{opacity:.6;transform:scale(1)}50%{opacity:1;transform:scale(1.3)}}'}</style>
</div>;
}
