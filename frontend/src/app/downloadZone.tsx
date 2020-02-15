import React from 'react';
import { Line } from 'shared/base/line';
import { Button } from 'shared/base/button';

import './downloadZone.scss';

export const DownloadZone: React.FC = () => {
  return (
    <Line className="downloadZone">
      <Line className="card container" justifyContent="around" alignItems="center">
        <Button buttonType="primary" label="Предпросмотр"></Button>
        <Button buttonType="primary" label="Скачать"></Button>
      </Line>
    </Line>
  );
};
