import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NethkenAComponent } from './nethken-a/nethken-a.component';
import { AboutComponent } from './about/about.component';

const routes: Routes = [{ path: '', redirectTo: '/home', pathMatch: 'full'},
                        { path: 'home', component: HomeComponent },
                        { path: 'nethkenA', component: NethkenAComponent },
                        { path: 'about', component: AboutComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
