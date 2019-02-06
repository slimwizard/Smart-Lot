import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NethkenAComponent } from './nethken-a/nethken-a.component';

const routes: Routes = [{ path: '', redirectTo: '/home', pathMatch: 'full'},
                        { path: 'home', component: HomeComponent },
                        { path: 'nethkenA', component: NethkenAComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
