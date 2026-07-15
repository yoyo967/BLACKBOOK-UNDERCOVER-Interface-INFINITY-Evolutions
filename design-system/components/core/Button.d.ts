export interface ButtonProps {
  /** Visual style */
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}
/**
 * @startingPoint section="Core" subtitle="Cyan-fill, outline and ghost buttons" viewport="700x200"
 */
export function Button(props: ButtonProps): JSX.Element;
