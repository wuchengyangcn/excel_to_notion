def title(text):
  return {
    'title': [{
      'text': {
        'content': text
      }
    }]
  }

def cover(url):
  return {
    'type': 'external',
    'external': {
      'url': url
    }
  }

def icon(url):
  return {
    'type': 'external',
    'external': {
      'url': url
    }
  }

def heading(text):
  return {
    'object': 'block',
    'type': 'heading_1',
    'heading_1': {
      'rich_text': [{
        'type': 'text',
        'text': {'content': text}
      }]
    }
  }

def paragraph(text):
  return {
    'object': 'block',
    'type': 'paragraph',
    'paragraph': {
      'rich_text': [{
        'type': 'text',
        'text': {'content': text}
      }]
    }
  }

def bulleted_list_item(text, annotations={}):
  return {
    'object': 'block',
    'type': 'bulleted_list_item',
    'bulleted_list_item': {
      'rich_text': [{
        'type': 'text',
        'text': {
          'content': text
        },
        'annotations': annotations
      }],
      'children': []
    }
  }

# TODO
# database