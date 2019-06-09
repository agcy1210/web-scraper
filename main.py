#scrapes the name, pic, designation and company details and saves to speakers.csv
import scrapy

class SpeakerDetails(scrapy.Spider):
    name = "SpeakerDetails"
    start_urls = ['https://www.ai-expo.net/europe/speakers/']

    def parse(self, response):
        for speaker,speaker_card in zip(response.css('div.speaker-key-details-expand'),response.css('div.speaker-top-expand')):
            try:
                company = speaker.css('h4::text')[1].get()
            except IndexError:
                company = ''

            yield {
                'Speaker Name': speaker.css('h3::text').get(),
                'Display Pic url':speaker_card.css('img').attrib['src'],
                'Designation': speaker.css('h4::text')[0].get(),
                'Company': company,
            }

