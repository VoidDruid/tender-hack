import React, { useState, useMemo, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Line } from 'shared/base/line';
import { TextBoxField } from 'shared/fields/textBoxField';
import { Button } from 'shared/base/button';
import { List } from 'app/list';
import { OptionsType } from 'data/model';
import { getRulesAsync } from 'data/file/action';

import './entityControl.scss';

interface ModelType {
  [key: string]: OptionsType;
}

interface Props {
  getModel: (model: ModelType) => void;
}

export const EntityControl: React.FC<Props> = ({ getModel }) => {
  const [model, setModel] = useState<ModelType>({});
  const [name, setName] = useState<string>();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRulesAsync());
  }, []);

  useEffect(() => {
    let obj: ModelType = {};
    for (const key in model) {
      if (key != '') obj = { ...obj, [key]: model[key] };
    }
    getModel(model);
  }, [model]);

  const headers = useMemo(() => {
    return Object.keys(model);
  }, [model]);

  return (
    <>
      <Line justifyContent="between" className="entityControl">
        <Line>
          <TextBoxField name="" value={name} onChange={(value: string) => setName(value)}></TextBoxField>
          <Button
            className="button"
            buttonType="light"
            label="Добавить поле"
            onClick={() => {
              if (name && name != '') {
                setModel({
                  ...model,
                  [`${name}`]: {}
                });
                setName('');
              }
            }}></Button>
        </Line>
      </Line>
      <Line vertical className="list">
        <List
          headers={headers}
          options={model}
          onAddOptions={(key: string, options: OptionsType) => setModel({ ...model, [key]: options })}
          onDelete={(key: string) => {
            const newModel = { ...model };
            delete newModel[key];
            setModel(newModel);
          }}
        />
      </Line>
    </>
  );
};
