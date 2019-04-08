import { Component } from '@angular/core';
import {
  transition,
  trigger,
  query,
  style,
  animate,
  group,
  animateChild
} from '@angular/animations';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  animations: [
    trigger('fadeAnimation', [

      transition( '* => *', [

          query(':enter', 
              [
                  style({ opacity: 0 })
              ], 
              { optional: true }
          ),

          query(':leave', 
              [
                  style({ opacity: 1 }),
                  animate('0.2s', style({ opacity: 0 }))
              ], 
              { optional: true }
          ),

          query(':enter', 
              [
                  style({ opacity: 0 }),
                  animate('0.2s', style({ opacity: 1 }))
              ], 
              { optional: true }
          )

      ])

  ])]
})
export class AppComponent {
  title = 'SMART LOT';
  aboutPageActive: boolean = false
  nightMode: boolean = false

  onAboutPage() {
    this.aboutPageActive = !this.aboutPageActive
  }

  changeVisibility() {
    var i:number; 

    this.nightMode = !this.nightMode;
    if (this.nightMode === true) {
      document.body.style.backgroundColor = "#2d2d2d"
      document.body.style.color = "#edf3ff"
      document.body.className = 'night-mode'
      for (i=0; i<document.getElementsByClassName('icon').length; i++) {
        document.getElementsByClassName('icon')[i].setAttribute("style","fill:white")
      }
      

    }
    else {
      document.body.style.backgroundColor = "white"
      document.body.style.color = "black"
      document.body.className = ''
      for (i=0; i<document.getElementsByClassName('icon').length; i++) {
        document.getElementsByClassName('icon')[i].setAttribute("style","fill:black")
      }
    }
  }
}


