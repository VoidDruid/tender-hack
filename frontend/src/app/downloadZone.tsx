import React, { useCallback } from 'react';
import { Line } from 'shared/base/line';
import { Button } from 'shared/base/button';
import './downloadZone.scss';
import { useSelector } from 'react-redux';
import { StoreType } from 'core/store';

export const DownloadZone: React.FC = () => {
  const file= useSelector((state: StoreType) => state.file.file);
  const loadFile=useCallback(()=>{
    if (file!='') {
      var element = document.createElement('a');
      element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(file));
      element.setAttribute('download', 'test.xml');
      element.style.display = 'none';
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    }
  },[file]);

  return (
    <Line className="downloadZone">
      <Line className="card container" justifyContent="around" alignItems="center">
        <Button buttonType="primary" label="Предпросмотр"></Button>
        <Button disabled={file==''} buttonType="primary" onClick={loadFile} label="Скачать"></Button>
      </Line>
    </Line>
  );
};
