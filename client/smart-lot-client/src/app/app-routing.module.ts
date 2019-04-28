import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { NethkenAComponent } from './components/nethken-a/nethken-a.component';
import { AboutComponent } from './components/about/about.component';
import { LotComponent } from './components/lot/lot.component'

  // ADD_LOT: New lots need to be routed to LotComponent

const routes: Routes = [{ path: '', redirectTo: '/home', pathMatch: 'full'},
                        { path: 'home', component: HomeComponent },
                        { path: 'nethkenA', component: NethkenAComponent },
                        { path: 'nethkena', component: LotComponent },
                        { path: 'grahama', component: LotComponent },
                        { path: 'about', component: AboutComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
