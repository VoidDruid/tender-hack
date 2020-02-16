import React, { useCallback, useState, useMemo } from 'react';
import { Line } from 'shared/base/line';
import './uploadZone.scss';
import { Icon } from 'shared/base/icon';
import { ActionType } from 'data/actionTypes';
import { Button } from 'shared/base/button';
import { useDispatch } from 'react-redux';
import { setFile as setUploadFile } from 'data/file/action';

import { RepeatPanel } from './repeatPanel';

export const UploadZone: React.FC = () => {
  const dispatch = useDispatch();
  const [upload, setUpload] = useState<boolean>(false);

  const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setUpload(true);
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
        setUpload(false);
        console.log(request.responseText);
        dispatch(setUploadFile(request.responseText));
      }
    };
  }, []);

  const uploadFile = useCallback(() => {}, []);
  return (
    <RepeatPanel action={uploadFile} actionType={ActionType.FILE_UPLOADFILE}>
      <Line className="uploadZone">
        <Line className="card container upload-container" justifyContent="around" alignItems="center">
         {upload && ( <div className="spinner-border text-primary" role="status">
            <span className="sr-only">Loading...</span>
          </div>)}
         {!upload&& ( <form encType="multipart/form-data" action="http://spacehub.su/api/format_excel?id=0" method="POST">
            <Line alignItems="center" justifyContent="center">
              <Icon className="img-upload" name="upload"></Icon>
            </Line>
            <Line alignItems="center" mt="3">
              <input id="file-input" className="input-upload" type="file" onChange={e => onChange(e)}></input>
              <label htmlFor="file-input">Выберите файл </label>
            </Line>
          </form>)}
        </Line>
      </Line>
    </RepeatPanel>
  );
};
