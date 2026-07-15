export interface QRPanelProps {
  /** Destination URL shown below the code (mono) */
  url: string;
  /** QR square size in px */
  size?: number;
}
/**
 * @startingPoint section="Book" subtitle="QR placeholder + mono URL for back-cover repo link" viewport="700x140"
 */
export function QRPanel(props: QRPanelProps): JSX.Element;
