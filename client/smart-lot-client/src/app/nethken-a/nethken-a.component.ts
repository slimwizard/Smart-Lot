import { Component, OnInit } from '@angular/core';
import { MatCardModule, MatButtonModule } from '@angular/material'

@Component({
  selector: 'app-nethken-a',
  templateUrl: './nethken-a.component.html',
  styleUrls: ['./nethken-a.component.css']
})
export class NethkenAComponent implements OnInit {

  constructor() { }
  selected: boolean = true;

  selectId(id: number) {
    console.log("hello")
    this.selected = !this.selected;
  }

  ngOnInit() {
  }

}
