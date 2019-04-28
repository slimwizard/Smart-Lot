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
import { CookieService } from 'ngx-cookie-service';


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
  nightMode: boolean
  colorblindMode: boolean
  colorblindCookie: string

  constructor(private cookie:CookieService){}

  ngOnInit(){
    var i:number
    if (this.cookie.get('colorblindModeCookie') === 'true') {
      this.colorblindMode = true
    }
    else{
      this.colorblindMode = false
    }

    if (this.cookie.get('nightModeCookie') === 'true'){
      this.nightMode = true
    }
    else{
      this.nightMode = false
    }
  }

  ngDoCheck() {
    if (this.cookie.get('colorblindModeCookie') === 'true') {
      this.colorblindMode = true
    }
    else{
      this.colorblindMode = false
    }

    if (this.cookie.get('nightModeCookie') === 'true'){
      this.nightMode = true
    }
    else{
      this.nightMode = false
    }
    var i:number
    if (this.colorblindMode === true){
      for (i=0; i<document.getElementsByClassName('openSpot').length; i++) {
        document.getElementsByClassName('openSpot')[i].setAttribute("style","fill:url(#pattern-circles) !important")
      }
      for (i=0; i<document.getElementsByClassName('takenSpot').length; i++) {
        document.getElementsByClassName('takenSpot')[i].setAttribute("style","fill:url(#diagonal-stripes-4-8) !important")
      }
    }

    if (this.nightMode === true){
      document.body.style.backgroundColor = "#2d2d2d"
      document.body.style.color = "#edf3ff"
      document.body.className = 'night-mode'
      for (i=0; i<document.getElementsByClassName('icon').length; i++) {
        document.getElementsByClassName('icon')[i].setAttribute("style","fill:white")
      }
    }
  }

  ngAfterViewChecked(){
    var i:number
    if (this.colorblindMode === true){
      for (i=0; i<document.getElementsByClassName('openSpot').length; i++) {
        document.getElementsByClassName('openSpot')[i].setAttribute("style","fill:url(#pattern-circles) !important")
      }
      for (i=0; i<document.getElementsByClassName('takenSpot').length; i++) {
        document.getElementsByClassName('takenSpot')[i].setAttribute("style","fill:url(#diagonal-stripes-4-8) !important")
      }
    }
    else{
      for (i=0; i<document.getElementsByClassName('openSpot').length; i++) {
        document.getElementsByClassName('openSpot')[i].setAttribute("style","fill:rgb(128, 231, 128) !important")
      }
      for (i=0; i<document.getElementsByClassName('takenSpot').length; i++) {
        document.getElementsByClassName('takenSpot')[i].setAttribute("style","fill:rgb(255, 112, 112) !important")
      }
    }

    if (this.nightMode === true){
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

    this.cookie.set('nightModeCookie', this.nightMode.toString())
  }

  changeColorblindMode() {
    var i:number;
    this.colorblindMode = !this.colorblindMode;
    if (this.colorblindMode === true) {
      for (i=0; i<document.getElementsByClassName('openSpot').length; i++) {
        document.getElementsByClassName('openSpot')[i].setAttribute("style","fill:url(#pattern-circles) !important")
      }
      for (i=0; i<document.getElementsByClassName('takenSpot').length; i++) {
        document.getElementsByClassName('takenSpot')[i].setAttribute("style","fill:url(#diagonal-stripes-4-8) !important")
      }
    }
    else{
      for (i=0; i<document.getElementsByClassName('openSpot').length; i++) {
        document.getElementsByClassName('openSpot')[i].setAttribute("style","fill:rgb(128, 231, 128) !important")
      }
      for (i=0; i<document.getElementsByClassName('takenSpot').length; i++) {
        document.getElementsByClassName('takenSpot')[i].setAttribute("style","fill:rgb(255, 112, 112) !important")
      }
    }
    this.cookie.set('colorblindModeCookie', this.colorblindMode.toString())
  }
}


