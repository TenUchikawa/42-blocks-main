// Disable no-unused-vars, broken for spread args
/* eslint no-unused-vars: off */
import { contextBridge, ipcRenderer, IpcRendererEvent } from 'electron';

export type ViewChannel = 'view-message';
export type ResultChannel = 'result-message';
const electronHandler = {
  ipcRenderer: {
    review(viewChannel:ViewChannel, func: (json: any) => void) {
      ipcRenderer.on(viewChannel, (_event, json) => func(json));
    },
    resultView(resultView:ResultChannel, func: (json: any) => void) {
      ipcRenderer.on(resultView, (_event, json) => func(json));
    },
  },
};

contextBridge.exposeInMainWorld('electron', electronHandler);

export type ElectronHandler = typeof electronHandler;
