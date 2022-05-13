import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ComponentsRoutingModule } from './components-routing.module';
import { AgGridModule } from 'ag-grid-angular';
import { VoicesComponent } from './voices/voices.component';
import { VoiceService } from '../services/voice.service';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    VoicesComponent
  ],
  imports: [
    CommonModule,
    ComponentsRoutingModule,
    AgGridModule.withComponents([]),
    HttpClientModule,
  ]
})
export class ComponentsModule { }
