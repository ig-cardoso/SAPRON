import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class AppService {
	private URL_BASE: string = "http://localhost:8000";

	constructor(private http: HttpClient) { }

	public showDados() {
		return this.http.get(this.URL_BASE);
	}
}
