export interface ChapterKickerProps {
  /** Series/collection name, e.g. "Interface Infinity Evolutions" */
  series: string;
  /** Optional volume/band label, e.g. "Band 1 · Master & System" */
  band?: string;
}
/**
 * @startingPoint section="Book" subtitle="Small mono series + band kicker for cover/chapter tops" viewport="700x120"
 */
export function ChapterKicker(props: ChapterKickerProps): JSX.Element;
