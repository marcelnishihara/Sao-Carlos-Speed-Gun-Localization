source = "https://saocarlosagora.com.br/"
regex = r"<\/svg>Radar (.*)</h2><div class=\"clear\"></div><div class=\"spacer20\"></div><section class=\"radar\"><ul>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>.*<li><big>([0-9]{2}).*<h4>(.*)<\/h4>"
regex_date = r"([0-9]+)\/([0-9]+)"

colors = {
    "err" : "\033[91m",
    "end" : "\033[m",
    "success" : "\033[92m",
    "warning" : "\033[93m"
}