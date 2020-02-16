export interface FieldType {
  index: string;
  name: string;
  is_multiple?: boolean;
  parent_of?: string;
}

export interface RuleType {
  name: string;
  type: string;
  fields: FieldType[];
}
