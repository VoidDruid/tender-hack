import React, { useState, useCallback, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { Line } from 'shared/base/line';
import { getRulesAsync, saveRulesAsync } from 'data/file/action';
import { EntityControl } from 'app/entityControl';
import { Button } from 'shared/base/button';
import { RuleType, FieldType } from 'data/file/models';
import { TextBoxField } from 'shared/fields/textBoxField';
import { OptionsType } from 'data/model';

import './processControl.scss';

export const ProcessControl: React.FC = () => {
  const [model, setModel] = useState<{ [key: string]: RuleType }>({});
  const [name, setName] = useState<string>();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRulesAsync());
  }, []);

  const onSaveCallback = useCallback(() => {
    const a: RuleType[] = [];
    for (const key in model) {
      a.push(model[key]);
    }
    dispatch(saveRulesAsync(a));
  }, [model]);

 const getEntities = useCallback(() => {
    const result: JSX.Element[] = [];
    for (const key in model) {
      result.push(
        <div key={key} className="entity">
          <div className="title">{model[key].name}</div>
          <EntityControl
            getModel={(m: { [key: string]: OptionsType }) => {
              const arr: FieldType[] = [];
              for (const key in m) {
                const options = m[key];
                let res: FieldType = { index: -1, name: key };
                if (options.isMultiple) res.is_multiple = options.isMultiple;
                if (options.parent) res.parent_of = options.parent;
                arr.push(res);


              }
              let i = 0;
              arr.forEach(x => {
                x.index = i;
                i++;
              });
              const k: RuleType = { name: key, type: 'array', fields: arr };
              setModel({ ...model, [key]: k });
            }}
          />
        </div>
      );
    }
    return result;
  }, [model]);

  return (
    <Line className="processControl">
      <Line className="card container">
        <Line justifyContent="between" className="buttonEntity">
          <Line vertical>
            <Line>
              <TextBoxField name="" value={name} onChange={(value: string) => setName(value)}></TextBoxField>
              <Button
                label="Добавить сущность"
                onClick={() => {
                  if (name && name != '') {
                    const newModel = { ...model, [name]: { name, type: 'array', fields: [] } };
                    setModel(newModel);
                  }
                  setName('');
                }}
                buttonType="primary"
                className="addEntityButton"></Button>
            </Line>
            {getEntities()}
          </Line>
          <Button label="Сохранить" onClick={onSaveCallback} buttonType="primary" className="saveButton"></Button>
        </Line>
      </Line>
    </Line>
  );
};
