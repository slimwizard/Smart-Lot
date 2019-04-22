import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { NethkenAComponent } from './components/nethken-a/nethken-a.component';
import { AboutComponent } from './components/about/about.component';
import { LotComponent } from './src/app/components/lot/lot.component';

const routes: Routes = [{ path: '', redirectTo: '/home', pathMatch: 'full'},
                        { path: 'home', component: HomeComponent },
                        { path: 'nethkenA', component: NethkenAComponent },
                        { path: 'lot', component: LotComponent},
                        { path: 'about', component: AboutComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
