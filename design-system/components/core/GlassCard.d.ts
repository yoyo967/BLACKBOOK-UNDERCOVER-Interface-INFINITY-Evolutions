export interface GlassCardProps {
  /** Use the stronger blur/saturation variant */
  strong?: boolean;
  /** Force the cyan glow shadow regardless of strong */
  glow?: boolean;
  children: React.ReactNode;
}
/**
 * @startingPoint section="Core" subtitle="Blurred glass panel, the brand's base surface" viewport="700x260"
 */
export function GlassCard(props: GlassCardProps): JSX.Element;
