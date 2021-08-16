import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders  } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UploadFilesService {

  private url: string;

    constructor(private _http: HttpClient) { 
        this.url = 'http://localhost:8000';
    }

    

    uploadfile(file : File){
      const formData:FormData = new FormData();
      formData.append('file', file);
      return this._http.post(this.url+'/images/imagenproccessorAPI',formData);
  }
}
