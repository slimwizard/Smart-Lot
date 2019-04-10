import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app.component';
import { MatExpansionModule, MatCardModule, MatButtonModule, MatListModule, MatProgressSpinnerModule, MatDividerModule, MatTooltipModule, MatDialogModule } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './components/home/home.component';
import { NethkenAComponent } from './components/nethken-a/nethken-a.component';
import { AboutComponent } from './components/about/about.component';
<<<<<<< HEAD
=======
import { LotModalComponent } from './components/nethken-a/lot-modal/lot-modal.component'
>>>>>>> 23b13cf8024acdc6b51480f21c293ec1ac5d4048

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NethkenAComponent,
    AboutComponent,
    LotModalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatExpansionModule,
    MatCardModule,
    MatButtonModule,
    MatListModule,
    MatProgressSpinnerModule,
    HttpClientModule,
    MatDividerModule,
    MatTooltipModule,
    MatDialogModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  entryComponents: [LotModalComponent]
})
export class AppModule { }
