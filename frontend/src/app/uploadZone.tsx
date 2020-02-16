import React, { useCallback, useState } from 'react';
import { Line } from 'shared/base/line';
import './uploadZone.scss';
import { useDispatch } from 'react-redux';
import { uploadFileAsync } from 'data/file/action';
import { Icon } from 'shared/base/icon';
import { ActionType } from 'data/actionTypes';

import { RepeatPanel } from './repeatPanel';

export const UploadZone: React.FC = () => {
  const dispatch = useDispatch();

  const [typeFile, setTypeFile] = useState<string>();
  const [file, setFile] = useState<string>();

  const onChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    const reader = new FileReader();
    const form = new FormData();
    reader.readAsArrayBuffer(e.target.files[0]);
    form.append('file', e.target.files[0]);
    reader.onload = e => {
      var request = new XMLHttpRequest();
      request.open('POST', 'http://spacehub.su/api/format_excel?id=1');
      request.setRequestHeader('contentType', 'multipart/form-data');
      request.send(form);
    };
  }, []);

  const uploadFile = useCallback(() => {
    //dispatch(uploadFileAsync({id:0, file: file}));
  }, []);

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
