{% if states.conference_ended %}

    <p class="small">19 мая в&nbsp;Санкт-Петербурге прошла конференция, посвященная юзабилити и&nbsp;проектированию пользовательского взаимодействия.</p>

    <p class="small">Уже опубликованы презентации докладов, а так же  <a href="http://www.facebook.com/media/set/?set=oa.344384208963349&type=1" target="_blank">фотографии с конференции</a>. Видеозаписи докладов вы можете посмотреть на <a href="https://vimeo.com/channels/profsoux2012" target="_blank">нашем канале</a>.</p>

    <p class="small">Спасибо всем, кто <a href="http://profsoux.ru/organizers/">сделал эту конференцию</a>!</p>

    <p><a href="{{ registration_url }}" class="btn btn-signup btn-primary btn-large">Хочу принять участие в&nbsp;ProfsoUX 2013</a>

{% else %}

    {% if states.registration = "waiting" %}
        {% if event.registration_start %}
            <p>Приём заявок на участие в конференции «ProfsoUX» откроется <nobr>{{ event.registration_start }}</nobr></p>
        {% endif %}

    {% elif states.registration = "active" %}
        <p><a href="/registration/" class="btn btn-signup btn-primary btn-large">Принять участие</a>

            <small>Торопитесь! Количество мест ограничено.</small><br />
            {% if event.registration_end %}
            Приём заявок прекращается
            {{ event.registration_end }}
            {% endif %}
        </p>

        <p>Тезисы докладов принимаются <nobr>до 1 апреля 2013 года</nobr> по&nbsp;адресу:
            <a href="mailto:pc-chairs@ux-spb.ru"><nobr>pc-chairs@ux-spb.ru</nobr></a>.</p>
    {% else %}
        <p><small>Приём заявок на участие в конференции завершён<br />
            Вы сможете присоединиться к онлайн-трансляции. Трансляция начнётся в 12:30 на нашем сайте.</small></p>
    {% endif %}

    {% if counts.participants %}
        <p>Уже идут: {{ counts.participants }}. <a href="/people/">Кто идёт? »</a></p>
    {% endif %}

{% endif %}

{% include "inc/btn-share.inc" %}