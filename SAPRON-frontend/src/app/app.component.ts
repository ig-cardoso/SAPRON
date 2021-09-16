import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';

@Component({
	selector: 'app-root',
	template: '',
	styles: []
})
export class AppComponent implements OnInit {
	title = 'SAPRON-frontend';
	
	constructor(private appService: AppService) {}

	ngOnInit(): void {
		this.show();
	}

	show() {
		this.appService.showDados().subscribe(response => {
			console.log('Dados!');
		});
	}

}
