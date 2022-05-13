import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Voice } from '../models/voice.model';

const baseUrl = 'http://localhost:8080/api/api';
@Injectable({
  providedIn: 'root'
})
export class VoiceService {

  constructor(private http: HttpClient) { }
  fetchAll(): Observable<Voice[]> {
    return this.http.get<Voice[]>(baseUrl);
  }
}
