import React from 'react';
import { Line } from 'shared/base/line';
import { Icon } from 'shared/base/icon';

import './progressControl.scss';

export const ProgressControl: React.FC = () => {
  return (
    <Line className="progressControl">
      <Line className="card container" justifyContent="around" alignItems="center">
        <div className="text-progress">Задание параметров</div>
        <Icon name="arrow-right"></Icon>
        <div className="text-progress">Загрузка файла</div>
        <Icon name="arrow-right"></Icon>
        <div className="text-progress">Выгрузка файла</div>
      </Line>
    </Line>
  );
};
