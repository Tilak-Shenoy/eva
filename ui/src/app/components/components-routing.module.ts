import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VoicesComponent } from './voices/voices.component';

export const routes: Routes = [
  { path: '', redirectTo: 'voices', pathMatch: 'full' },
  { path: 'voices', component: VoicesComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ComponentsRoutingModule { }
