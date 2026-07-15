export interface BadgeProps {
  tone?: 'neutral' | 'signal' | 'outline';
  /** Render in mono uppercase (used for status/ledger-style tags) */
  mono?: boolean;
  children: React.ReactNode;
}
/**
 * @startingPoint section="Core" subtitle="Status pill / mono ledger tag" viewport="700x160"
 */
export function Badge(props: BadgeProps): JSX.Element;
