import React, { useCallback, useState, useMemo } from 'react';
import { Line } from 'shared/base/line';
import './uploadZone.scss';
import { Icon } from 'shared/base/icon';
import { ActionType } from 'data/actionTypes';
import { Button } from 'shared/base/button';

import { RepeatPanel } from './repeatPanel';

export const UploadZone: React.FC = () => {
  const [file, setFile] = useState<string>();

  useMemo(() => {
    console.log(file);
  }, [file]);

  const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const reader = new FileReader();
    const form = new FormData();
    reader.readAsArrayBuffer(e.target.files[0]);
    form.append('file', e.target.files[0]);

    var request = new XMLHttpRequest();
    request.open('POST', 'http://spacehub.su/api/format_excel?id=1');
    request.setRequestHeader('contentType', 'multipart/form-data');
    request.send(form);
    request.onload = function() {
      if (request.status == 200) {
        setFile(request.response);
        console.log('type   ', typeof request.response);
      }
    };
  }, []);

  const download = useCallback(
    (file: string) => {
      if (file) {
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/xml;charset=utf-8,' + encodeURIComponent(file));
        element.setAttribute('download', 'test.yaml');
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
      }
    },
    [file]
  );

  const uploadFile = useCallback(() => {}, []);
  return (
    <RepeatPanel action={uploadFile} actionType={ActionType.FILE_UPLOADFILE}>
      <Line className="uploadZone">
        <Line className="card container upload-container" justifyContent="around" alignItems="center">
          <form encType="multipart/form-data" action="http://spacehub.su/api/format_excel?id=0" method="POST">
            <Line alignItems="center" justifyContent="center">
              <Icon className="img-upload" name="upload"></Icon>
            </Line>
            <Line alignItems="center" mt="3">
              <input id="file-input" className="input-upload" type="file" onChange={e => onChange(e)}></input>
              <label htmlFor="file-input">Выберите файл </label>
            </Line>
          </form>
        </Line>
      </Line>
    </RepeatPanel>
  );
};
