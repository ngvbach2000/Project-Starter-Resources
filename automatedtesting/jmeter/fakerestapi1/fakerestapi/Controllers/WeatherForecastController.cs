using Microsoft.AspNetCore.Mvc;

namespace fakerestapi.Controllers
{
    [ApiController]
    public class WeatherForecastController : ControllerBase
    {

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger)
        {
            _logger = logger;
        }

        [HttpGet("api/v1/employees")]
        public IActionResult Get()
        {
            return Ok();
        }

        [HttpPost("api/v1/create")]
        public IActionResult Post()
        {
            return Ok();
        }
    }
}