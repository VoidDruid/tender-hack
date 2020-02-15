import React, { useState } from 'react';
import { Line } from 'shared/base/line';
import { Icon } from 'shared/base/icon';
import { OptionsType } from 'data/model';
import { OptionsPanel } from 'app/optionsPanel';

import './itemCard.scss';

interface Props {
  onDelete: () => void;
  onAddOptions: (options: OptionsType) => void;
  headers: string[];
  originalKey: string;
}

export const ItemCard: React.FC<Props> = ({ onDelete, children, onAddOptions, headers, originalKey }) => {
  const [showTip, setShowTip] = useState(true);
  return (
    <Line className="card itemCard" justifyContent="between" alignItems="center">
      <Line vertical className="content">
        <div className="children">{children}</div>
        {showTip && (
          <div
            className="options"
            onClick={() => {
              setShowTip(false);
            }}>
            Задать параметры
          </div>
        )}
        {!showTip && (
          <OptionsPanel
            headers={headers}
            hideOptions={() => {
              setShowTip(true);
              onAddOptions({});
            }}
            originalKey={originalKey}
            onAddOptions={onAddOptions}></OptionsPanel>
        )}
      </Line>
      <div className="icon">
        <Icon name="times" onClick={onDelete}></Icon>
      </div>
    </Line>
  );
};
