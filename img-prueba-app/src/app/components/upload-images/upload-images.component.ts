import { Component, OnInit } from '@angular/core';
import { UploadFilesService } from 'src/app/services/upload-files.service';
import { HttpEventType, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-upload-images',
  templateUrl: './upload-images.component.html',
  styleUrls: ['./upload-images.component.css']
})
export class UploadImagesComponent implements OnInit {
  
  public fileuploaded:any;
  public data:any;
  public isValidImg:boolean;
  public url:any;
 

  constructor(private _uploadService: UploadFilesService) { 
    this.isValidImg = false;
  }

  ngOnInit(): void {
  }

  selectFiles(event:any){
    const files = event.target.files[0];
    var type = files.type;
    

    if ( !(type == "image/jpeg")) {
      alert('invalid format!');     
      this.isValidImg = false;
    }else{
      this.fileuploaded = files;
      this.isValidImg = true;

      var reader = new FileReader();
		  reader.readAsDataURL(event.target.files[0]);
		
		reader.onload = (_event) => {
			this.url = reader.result; 
		}
     
    }
  }

  uploadFiles(){
    if(this.fileuploaded){
      this._uploadService.uploadfile(this.fileuploaded).subscribe(
        result => {
          this.data = result;  
          console.log(this.data);            
        },
        error => {
          var errorMessage = <any>error;
          console.log(errorMessage); 
        }
        );
    }    
  }

  setNewDim(){
    

  }
}
