import { Component, OnInit } from '@angular/core';
import {MatDialogRef} from '@angular/material'

@Component({
  selector: 'app-lot-modal',
  templateUrl: './lot-modal.component.html',
  styleUrls: ['./lot-modal.component.scss']
})
export class LotModalComponent implements OnInit {

  constructor(private dialogRef: MatDialogRef<LotModalComponent>) {}

  onClick(): void {
    this.dialogRef.close()
    let body = document.getElementsByTagName('html')
    body[0].blur()
    }

  ngOnInit() {
  }

}
