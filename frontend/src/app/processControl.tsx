import React from 'react';
import { Line } from 'shared/base/line';

import './processControl.scss';

export const ProcessControl: React.FC = () => {
  return (
    <Line className="processControl">
      <Line className="card container" justifyContent="around" alignItems="center"></Line>
    </Line>
  );
};
