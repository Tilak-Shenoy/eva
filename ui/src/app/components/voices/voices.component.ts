import { Component, OnInit } from '@angular/core';
import { ColDef } from 'ag-grid-community';
import { Observable } from 'rxjs';
import { Voice } from 'src/app/models/voice.model';
import { VoiceService } from 'src/app/services/voice.service';

@Component({
  selector: 'app-voices',
  templateUrl: './voices.component.html',
  styleUrls: ['./voices.component.scss']
})
export class VoicesComponent implements OnInit {
  voices?: Observable<Voice[]>;
  colDefs: ColDef[] = []
  constructor(private voiceService: VoiceService) { }

  ngOnInit(): void {
    this.initializeGrid();
    this.loadGridData();
  }

  initializeGrid(): void {
    this.colDefs = [
      { field: 'id' },
      { field: 'language', sortable: true, filter: true },
      { field: 'country', sortable: true, filter: true },
      { field: 'locale', sortable: true, filter: true },
      { field: 'gender', sortable: true, filter: true },
      { field: 'voice_name', sortable: true, filter: true }
  ];
  }

  loadGridData(): void {
    // this.voiceService.fetchAll().subscribe((response: any) => {
    //   response.forEach((rec: Voice) => {
    //     this.voices.push(rec);
    //   });
    //   console.log(this.voices)
    // })

    this.voices = this.voiceService.fetchAll();
  
  }

}


