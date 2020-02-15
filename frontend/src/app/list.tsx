import React, { useMemo } from 'react';
import { ItemCard } from 'app/itemCard';
import { OptionsType } from 'data/model';

interface Props {
  options: { [key: string]: OptionsType };
  onDelete: (key: string) => void;
  onAddOptions: (key: string, options: OptionsType) => void;
  headers: string[];
}

export const List: React.FC<Props> = ({ onDelete, options, onAddOptions, headers }) => {
  const items = useMemo(() => {
    const arr: JSX.Element[] = [];
    for (const key in options) {
      arr.push(
        <ItemCard
          originalKey={key}
          headers={headers}
          key={key}
          onDelete={() => onDelete(key)}
          onAddOptions={(options: OptionsType) => onAddOptions(key, options)}>
          {key}
        </ItemCard>
      );
    }
    return arr;
  }, [options]);

  return <>{items}</>;
};
