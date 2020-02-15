import React from 'react';
import { Line } from 'shared/base/line';

import './uploadZone.scss';

export const UploadZone: React.FC = () => {
  return (
    <Line className="uploadZone">
      <Line className="card container" justifyContent="around" alignItems="center"></Line>
    </Line>
  );
};