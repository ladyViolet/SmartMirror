/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "localhost", // Address to listen on, can be:
	                      // - "localhost", "127.0.0.1", "::1" to listen on loopback interface
	                      // - another specific IPv4/6 to listen on a specific interface
	                      // - "0.0.0.0", "::" to listen on any interface
	                      // Default, when address config is left out or empty, is "localhost"
	port: 8080,
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], // Set [] to allow all IP addresses
	                                                       // or add a specific IPv4 of 192.168.1.5 :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
	                                                       // or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
	                                                       // ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false, 		// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true

	language: "en",
	timeFormat: 24,
	units: "metric",
	// serverOnly:  true/false/"local" ,
			     // local for armv6l processors, default
			     //   starts serveronly and then starts chrome browser
			     // false, default for all  NON-armv6l devices
			     // true, force serveronly mode, because you want to.. no UI on this device

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "Feiertage",
			position: "top_left",
			config: {
				calendars: [
					{
						symbol: "calendar-check",
						url: "webcal://www.calendarlabs.com/ical-calendar/ics/46/Germany_Holidays.ics"					}
				]
			}
		},
		{
			module: "compliments",
			position: "lower_third"
		},
		{
			module: "currentweather",
			position: "top_right",
			config: {
				location: "Regensburg",
				locationID: "", //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "ff7faebc9c8c34ad7992a4e29e89744",
				lang: "de",
				//showFeelsLike: true,
				//showWindDirection: true,
				//onlyTemp: true
			}
		},
		{
			module: "weatherforecast",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				location: "Regensburg",
				locationID: "2849483", //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				appid: "ff7faebc9c8c34ad7992a4e29e89744",
				lang: "de"
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "FAZ",
						url: "https://www.faz.net/rss/aktuell/"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
		/*{
			disabled: false,
			module: "MMM-Selfieshot",
			config: {
				debug: false, // You can get more detailed log. If you have an issue, try to set this to true.
				storePath: "./photos", // No need to modify.
				width:1280,
				height:720, // In some webcams, resolution ratio might be fixed so these values might not be applied.
				quality: 100, //Of course.
				device: null, // `null` for default camera. Or,
				// device: "USB Camera" or "/video/video11" <-- See the backend log to get your installed camera name.
				shootMessage: "Smile!",
				shootCountdown: 5, // 5,4,3,2,1,0 then shutter.
				displayCountdown: true,
				displayResult: true,
				playShutter: true,
				shutterSound: "shutter.mp3",
				useWebEndpoint: "selfie", // This will activate 'https://YOUR_MM_IP_OR_DOMAIN:PORT/selfie [POST]' as web API endpoint.
				resultDuration: 1000 * 5,
				sendTelegramBot: false,
			}	
		},*/	
		  /*{
		    module: 'MMM-BackgroundSlideshow',
		    position: 'fullscreen_below',
		    config: {
		      imagePaths: ['modules/MMM-BackgroundSlideshow/exampleImages/'],
		      transitionImages: true,
		      randomizeImageOrder: true,
		    },
		  },*/
		]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
