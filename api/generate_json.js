// api/generate_json.js
export default function handler(req, res) {
	// 仮のデータを作成
	const data = {
		"dow": {
			"forecast": [
			{ "date": "2023-01-01", "value": 32500.35 },
			{ "date": "2023-01-02", "value": 32800.75 },
			]
		},
		"sp500": {
			"forecast": [
			{ "date": "2023-01-01", "value": 4200.50 },
			{ "date": "2023-01-02", "value": 4225.75 },
			]
		}
	};
	
	// レスポンスとしてJSONデータを返す
	res.status(200).json(data);
}
